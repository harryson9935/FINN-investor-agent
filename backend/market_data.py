import yfinance as yf
from typing import Dict, Optional, List

class MarketDataEngine:
    @staticmethod
    def evaluate_ticker(ticker: str, price_thresh_pct: float = 4.0, vol_thresh_ratio: float = 2.0) -> Optional[Dict]:
        try:
            asset = yf.Ticker(ticker)
            hist = asset.history(period="1mo")
            if len(hist) < 20:
                return None
            
            latest = hist.iloc[-1]
            prev = hist.iloc[-2]
            avg_vol_20d = hist['Volume'].iloc[-21:-1].mean()
            
            close = latest['Close']
            change_pct = ((close - prev['Close']) / prev['Close']) * 100.0
            vol_ratio = latest['Volume'] / avg_vol_20d if avg_vol_20d > 0 else 1.0
            
            flag_price = abs(change_pct) >= price_thresh_pct
            flag_volume = vol_ratio >= vol_thresh_ratio
            
            if flag_price or flag_volume:
                return {
                    "ticker": ticker,
                    "close": round(close, 2),
                    "change_pct": round(change_pct, 2),
                    "volume": int(latest['Volume']),
                    "avg_vol_20d": int(avg_vol_20d),
                    "vol_ratio": round(vol_ratio, 2),
                    "flags": {
                        "unusual_price": flag_price,
                        "unusual_volume": flag_volume
                    }
                }
        except Exception:
            return None
        return None

    @classmethod
    def scan_portfolio(cls, tickers: List[str]) -> List[Dict]:
        results = []
        for t in tickers:
            signal = cls.evaluate_ticker(t)
            if signal:
                results.append(signal)
        return results
