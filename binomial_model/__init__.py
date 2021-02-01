import math


class BinomialModel:
    def __init__(self):
        pass

    # modified from https://www.josephthurman.com/binomial4.html
    def american_call_price(self, S, K, T, r, vol, N):
        dt = T/N
        u = math.exp(vol * math.sqrt(dt))
        d = 1/u
        p = (math.exp(r * dt) - d)/(u - d)
        C = {}

        for m in range(0, N+1):
            C[(N, m)] = max(S * (u ** m) * (d ** (N-m)) - K, 0)

        for k in range(N-1, -1, -1):
            for m in range(0, k+1):
                future_val = math.exp(-r * dt) * (p * C[(k+1, m+1)] + (1-p) * C[(k+1, m)])
                intrinsic_val = max(S - K, 0)
                C[(k, m)] = max(future_val, intrinsic_val)

        return C[(0, 0)]

    # modified from https://www.josephthurman.com/binomial4.html
    def redeemable_american_call_price(self, S, K, T, r, vol, N, redemption_price):
        dt = T / N
        u = math.exp(vol * math.sqrt(dt))
        d = 1 / u
        p = (math.exp(r * dt) - d) / (u - d)
        C = {}

        for m in range(0, N + 1):
            C[(N, m)] = max(S * (u ** m) * (d ** (N - m)) - K, 0)

        for k in range(N - 1, -1, -1):
            for m in range(0, k + 1):
                future_val = math.exp(-r * dt) * (p * C[(k + 1, m + 1)] + (1 - p) * C[(k + 1, m)])
                intrinsic_val = max(S - K, 0)
                american_px = max(future_val, intrinsic_val)
                redemption_payoff = redemption_price - K
                C[(k, m)] = min(american_px, redemption_payoff)

        return C[(0, 0)]


if __name__ == '__main__':
    bm = BinomialModel()
    # print(bm.american_call_price(100, 115, 0.25, 0.015, 0.2, 1000))  # should == 0.42746...
    # print(bm.american_call_price(11.34, 48.74, 2.5, 0.0000001, 0.8, 1000))
    # print(bm.redeemable_american_call_price(11.5, 11.42, 4.5, 0.0000001, 0.79, 1000, 18))
    print(bm.american_call_price(373.66, 300, 0.97, 0.0000001, 0.2215, 1000))
    print(bm.american_call_price(373.66, 445, 0.97, 0.0000001, 0.2215, 1000))
