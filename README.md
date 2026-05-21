# Binance Futures Trading Bot

A simple command-line trading bot built using Python and Binance Futures Testnet API.

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Command-line interface
- Input validation
- Logging system
- Binance Futures Testnet integration

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── cli.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
├── venv/
├── .env
├── requirements.txt
└── README.md

## Installation

Create virtual environment:

python -m venv venv

Activate virtual environment:

venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a `.env` file:

API_KEY=your_api_key
API_SECRET=your_api_secret

## Run MARKET Order

python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Run LIMIT Order

python bot/cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

## Logs

Logs are stored inside:

logs/trading_bot.log

Developed By Hashmita Poojari