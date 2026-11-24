# Say What Actually Broke — Elies87 entry

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Elies87/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Elies87/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty on make.fun.

## The line

> We lost your work. Not deleted — lost. The server crashed mid-save and the only backup was a Post-it that said ‘back up the server’. Try again.

One line of software error copy (143 characters) that tells the brutal truth — the server crashed mid-save and there was no real backup — and lands the joke in a single read, while still telling the user what to do next: try again.

## How it works

`main.py` is Python 3, standard library only. It writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), as UTF-8 text: one line
plus a trailing newline. The output is fully deterministic — running it twice
produces byte-identical files.

```sh
python3 main.py
# or, with an explicit output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
