class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> idxHMap = new HashMap<>();
        for(String s : strs) {
            String sCharCount = countCharacters(s);
            if(idxHMap.containsKey(sCharCount)) {
                idxHMap.get(sCharCount).add(s);
            }
            else {
                List<String> sList = new ArrayList<>();
                sList.add(s);
                idxHMap.put(sCharCount, sList);
            }
        }

        // Loop over enery element in the hashmap
        return new ArrayList<>(idxHMap.values());
    }

    private String countCharacters(String s) {
        int[] countChar = new int[26];

        int length = s.length();
        for(int i = 0  ; i < length ; i++) {
            char ch = s.charAt(i);
            int idx = ch - 'a';
            countChar[idx]++;
        }

        StringBuilder sb = new StringBuilder(0);
        for(int i = 0 ; i < countChar.length ; i++) {
            sb.append((char)(i +  'a'));
            sb.append(countChar[i]);
        }

        return sb.toString();
    }
}
