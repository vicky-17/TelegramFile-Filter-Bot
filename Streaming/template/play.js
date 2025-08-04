function openReport() {
    document.getElementById("myForm").style.display = "block";
}

function closeReport() {
    document.getElementById("myForm").style.display = "none";
}

function closeLinkModal() {
    document.getElementById("link-modal").style.display = "none";
}

function shareButton() {
    if (navigator.share) {
        const url = window.location.href;
        const title = document.title;
        navigator.share({
            title: title,
            text: "You can watch high-quality videos on this Stream page, one of the most powerful streaming platforms.\n\n" + title + "\n",
            url: url
        })
            .then(() => {
                console.log("Thanks for sharing!");
            })
            .catch(error => {
                console.log(`Couldn't share because of ${error.message}`);
            });
    } else {
        alert("Sorry, sharing isn't supported in this browser. Try Google Chrome or copy the link manually.");
    }
}

function showAdsLinkModal(link) {
    const modal = document.getElementById("link-modal");
    const timer = document.getElementById("link-timer");
    modal.style.display = "block";
    let countdown = 5;
    const interval = setInterval(() => {
        countdown--;
        timer.innerHTML = countdown;
        if (countdown === 0) {
            clearInterval(interval);
            timer.innerHTML = "";
            window.location.href = link;
            closeLinkModal();
        }
    }, 1000);
}

document.addEventListener("DOMContentLoaded", () => {
    Plyr.setup("#myVideo", {
        controls: [
            "play-large",
            "rewind",
            "audio",
            "play",
            "fast-forward",
            "progress",
            "current-time",
            "duration",
            "captions",
            "settings",
            "pip",
            "airplay",
            "fullscreen"
        ]
    });

    const themeToggleBtn = document.getElementById("theme-toggle-btn");
    let theme = localStorage.getItem("theme") || "dark";

    const setTheme = (theme) => {
        if (theme === "light") {
            document.body.classList.remove("bg-dark", "text-light");
            document.body.classList.add("bg-light", "text-dark");
            themeToggleBtn.innerHTML = '<i class="fa-solid fa-moon"></i> Dark Mode';
            themeToggleBtn.classList.replace("btn-light", "btn-dark");
        } else {
            document.body.classList.remove("bg-light", "text-dark");
            document.body.classList.add("bg-dark", "text-light");
            themeToggleBtn.innerHTML = '<i class="fa-solid fa-sun"></i> Light Mode';
            themeToggleBtn.classList.replace("btn-dark", "btn-light");
        }
    };

    themeToggleBtn.addEventListener("click", () => {
        const newTheme = document.body.classList.contains("bg-dark") ? "light" : "dark";
        setTheme(newTheme);
    });

    setTheme(theme);
});

function Open_Link(link) {
    if (link) {
        window.open(link, "_blank");
    }
}

function showLinkModal(link) {
    window.open(link, "_blank");
}

function Open_DL(link) {
    window.location.href = link.replace("replace", "dl");
}

function Open_TG(link) {
    window.location.href = link.replace("replace", "tg");
}

const videolink = window.location.href;
const streamlink = videolink.replace("/watch/", "/dl/");

function vlc_player() {
    const link = streamlink.replace(/^https?:\/\//, "");
    window.location.href = `vlc://${link}`;
}

function mx_player() {
    const link = streamlink.replace(/^https?:\/\//, "");
    window.location.href = `intent://${link}#Intent;scheme=https;package=com.mxtech.videoplayer.ad;action=android.intent.action.VIEW;end`;
}

function playit_player() {
    const link = streamlink.replace(/^https?:\/\//, "");
    window.location.href = `intent://${link}#Intent;package=com.playit.videoplayer;action=android.intent.action.VIEW;end`;
}

function streamDownload() {
    window.location.href = streamlink;
}

document.addEventListener("DOMContentLoaded", () => {
    const style = document.createElement("style");
    style.innerHTML = `
        @keyframes devBounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-4px);
            }
        }
        .dev-icon {
            display: inline-block;
            animation: devBounce 1.2s infinite;
            color: #0dcaf0;
            margin-left: 6px;
        }
        .footer-text {
            color: #0dcaf0;
            text-decoration: none;
        }
    `;
    document.head.appendChild(style);

    const footer = document.createElement("footer");
    footer.className = "py-2 text-center border-top border-secondary bg-dark text-light";

    const p = document.createElement("p");
    p.className = "mb-0";

    const a = document.createElement("a");
    a.href = "tg://resolve?domain=IM_JISSHU";
    a.target = "_blank";
    a.className = "footer-text";

    const icon = document.createElement("i");
    icon.className = "fa-solid fa-robot me-2";

    const text = document.createTextNode("Made by Vicky");

    const codeIcon = document.createElement("i");
    codeIcon.className = "fa-solid fa-laptop-code dev-icon";

    a.appendChild(icon);
    a.appendChild(text);
    a.appendChild(codeIcon);
    p.appendChild(a);
    footer.appendChild(p);
    document.body.appendChild(footer);
});