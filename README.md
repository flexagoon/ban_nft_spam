# Ban NFT Spam

A Telegram bot to ban NFT spam comments.

## Mechanism

This bot is based on a very simple heuristic: all of the NFT ad domains have an
`/encryption.js` file, so whenever a website which has that file is sent in the
chat, the bot deletes the message and bans the user. 

Therefore, there is a risk of false positives when using this bot.

## Deploying

You need to have `poetry` installed. If you don't already have it and just use
the `pip` command directly, you should uninstall Python and never touch it again.

1. Run `poetry install` to install all project dependencies.
2. Provide the bot token in a `TOKEN` environment variable. This can be done in a
`.env` file or witqh any other method of setting environment variables.
3. Run the bot with `poetry run python ban_nft_spam.py`
