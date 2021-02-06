def birthdayCakeCandles(candles):
    print(candles.count(max(candles))) 
candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
birthdayCakeCandles(candles)