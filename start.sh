if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/vicky-17/smart-telegram-filter-bot /smart-telegram-filter-bot
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /smart-telegram-filter-bot
fi
cd /smart-telegram-filter-bot
pip3 install -U -r requirements.txt
echo "Starting filter bot...."
python3 bot.py
