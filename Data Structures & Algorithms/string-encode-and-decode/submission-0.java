class Solution {
    final char DELIMITER = '#';

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for(String str : strs) {
            sb.append(str.length());
            sb.append(DELIMITER);
            sb.append(str);
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        int length = str.length();
        StringBuilder sb = new StringBuilder();
        ArrayList<String> toReturn = new ArrayList<>();

        int idx = 0;
        while(idx < length) {
            char ch = str.charAt(idx);

            if(ch == DELIMITER) {
                int lenOfWord = Integer.parseInt(sb.toString());
                sb = null;
                sb = new StringBuilder();

                toReturn.add(str.substring(idx+1, idx + lenOfWord + 1));
                idx += lenOfWord + 1;
            } else {
                sb.append(ch);
                idx++;
            }
        }

        return toReturn;
    }
}
