class Solution:
    def encode(self, strs: List[str]) -> str:
        enc_str = "".join([self.encode_str(st) for st in strs])
        print(enc_str)
        return enc_str

    def decode(self, s: str) -> List[str]:
        l = len(s)
        i = 0
        op = []
        while i < l:
            j = s.index("#", i)
            print(f"{i}:{j}")
            size = s[i:j]
            print(f"{size}")
            int_sz = int(size)
            end_idx = j+1+int_sz
            st = s[j+1:end_idx]
            print(f"{st}")
            op.append(st)
            i = end_idx
        return op

    def encode_str(self, s: str) -> str:
        l = len(s)
        return f"{l}#{s}"





