# swing-trader

OANDA-based forex trading project with Bollinger Band mean-reversion signals, real-time price streaming, backtesting, and FX news/calendar scrapers.

This is the **ancestor codebase** for the more advanced [Automated_trading_bot](https://github.com/Kaireega/Automated_trading_bot) project.

---

## Features

- **Live streaming bot** — multi-threaded price processing with Bollinger Band signals (`stream_bot/`)
- **Polling bot** — older architecture (`bot/`)
- **OANDA API client** — REST integration for candles, instruments, and account data
- **Backtesting** — moving-average crossover and EMA/MACD simulations (`simulation/`)
- **Web scraping** — FX calendar, Bloomberg, and Investing.com data (`scraping/`)
- **Exploration notebooks** — 15 Jupyter notebooks for strategy research

---

## Tech stack

- Python 3
- OANDA REST API (`requests`)
- pandas, python-dateutil
- BeautifulSoup (scraping)
- Jupyter notebooks

---

## Quick start

### 1. Install dependencies

```bash
git clone https://github.com/Kaireega/swing-trader.git
cd swing-trader
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure OANDA credentials

```bash
cp config.env.example config.env
# Edit config.env with your OANDA practice account credentials
```

| Variable | Description |
|----------|-------------|
| `OANDA_API_KEY` | OANDA API bearer token |
| `OANDA_ACCOUNT_ID` | OANDA account ID |
| `OANDA_URL` | API base URL (default: practice endpoint) |

### 3. Run

| Command | Purpose |
|---------|---------|
| `python run_bot.py` | Live streaming bot (primary entry point) |
| `python main.py` | Price streamer demo |
| `python api_tests.py` | API connectivity tests |
| `python scraping_tests.py` | Scraper tests |
| `python simulation/ma_cross.py` | MA crossover backtest |

Strategy parameters (pairs, Bollinger windows, risk) are configured in `stream_bot/settings.json`.

---

## Project structure

```
swing-trader/
├── run_bot.py              # Primary live bot entry point
├── main.py                 # Price streamer demo
├── api/oanda_api.py        # OANDA REST client
├── constants/defs.py       # Loads config.env
├── stream_bot/             # Active streaming architecture
├── bot/                    # Older polling-based bot
├── simulation/             # Backtest scripts
├── scraping/               # FX news/calendar scrapers
├── technicals/             # Indicators and patterns
├── exploration/            # Jupyter notebooks
└── data/                   # Cached instrument data
```

---

## Disclaimer

This bot connects to OANDA's **practice** API by default. Trading forex carries significant financial risk. Use paper trading to validate strategies before risking real capital. The author is not responsible for any financial losses.

---

## Related projects

- [Automated_trading_bot](https://github.com/Kaireega/Automated_trading_bot) — evolved multi-strategy fork with backtesting framework
- [full_forex_box](https://github.com/Kaireega/full_forex_box) — full-stack platform with dashboards
- [notificactionn-bot](https://github.com/Kaireega/notificactionn-bot) — AI-assisted trading with notifications

---

## Author

**Kai'ree Gay** — [GitHub](https://github.com/Kaireega)
