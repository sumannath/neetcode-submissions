class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sCharacters = countCharacters(s);
        HashMap<Character, Integer> tCharacters = countCharacters(t);

        return sCharacters.equals(tCharacters);
    }

    private HashMap<Character,Integer> countCharacters(String s) {
        HashMap<Character, Integer> charCount = new HashMap<>();

        int length = s.length();
        for(int i = 0  ; i < length ; i++) {
            char ch = s.charAt(i);
            if(charCount.containsKey(ch)) {
                charCount.put(ch, charCount.get(ch) + 1);
            } else {
                charCount.put(ch, 1);
            }
        }

        return charCount;
    }
}
