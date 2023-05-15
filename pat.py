(lambda s = input('Enter your string: '): print({i: s.count(i) for i in set(s)}))()
