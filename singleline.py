L = ["Hello", "World", 18, "Apple", None]

# 返回字符串小写，其他类型不变
L2 = list((s.lower() if isinstance(s, str) else s for s in L))

print(L2)
