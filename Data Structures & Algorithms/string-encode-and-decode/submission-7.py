class Solution:
    def encode(self, strs: List[str]) -> str:
        enc_str = "".join([self.encode_str(st) for st in strs])
        return enc_str

    def decode(self, s: str) -> List[str]:
        l = len(s)
        i = 0
        op = []
        while i < l:
            j = s.index("#", i)
            size = int(s[i:j])
            end_idx = j+1+size
            st = s[j+1:end_idx]
            op.append(st)
            i = end_idx
        return op

    def encode_str(self, s: str) -> str:
        l = len(s)
        return f"{l}#{s}"





