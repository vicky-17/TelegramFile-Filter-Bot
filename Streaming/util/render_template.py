import jinja2
from info import URL, LOG_CHANNEL
from utils import temp
from Streaming.bot import FilterBot
from Streaming.util.human_readable import humanbytes
from Streaming.util.file_properties import get_file_ids
from Streaming.server.exceptions import InvalidHash
from Template import jisshu_template
import urllib.parse
import logging
import aiohttp


async def render_page(id, secure_hash, src=None):
    file = await FilterBot.get_messages(int(LOG_CHANNEL), int(id))
    file_data = await get_file_ids(FilterBot, int(LOG_CHANNEL), int(id))
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f"link hash: {secure_hash} - {file_data.unique_id[:6]}")
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash

    src = urllib.parse.urljoin(
        URL,
        f"{id}/{urllib.parse.quote_plus(file_data.file_name)}?hash={secure_hash}",
    )

    tg_button = f"https://telegram.dog/{temp.U_NAME}"

    tag = file_data.mime_type.split("/")[0].strip()
    file_size = humanbytes(file_data.file_size)
    if tag in ["video", "audio"]:
        template_file = "Streaming/template/req.html"
    else:
        template_file = "Streaming/template/dl.html"
        async with aiohttp.ClientSession() as s:
            async with s.get(src) as u:
                file_size = humanbytes(int(u.headers.get("Content-Length")))

    with open(template_file) as f:
        template = jinja2.Template(f.read())

    file_name = file_data.file_name.replace("_", " ").replace(".", " ")

    return template.render(
        file_name=file_name,
        file_url=src,
        file_size=file_size,
        tg_button=tg_button,
        file_unique_id=file_data.unique_id,
        template_ne=jisshu_template.JISSHU_NAME,
        jisshu_disclaimer=jisshu_template.JISSHU_DISCLAIMER,
        jisshu_report_link=jisshu_template.JISSHU_REPORT_LINK,
        jisshu_colours=jisshu_template.JISSHU_COLOURS,
    )
