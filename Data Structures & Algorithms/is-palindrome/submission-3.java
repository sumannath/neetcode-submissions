class Solution {
    public boolean isPalindrome(String s) {
        int len = s.length();
        int headIdx = 0, tailIdx = len - 1;

        try {
            while (headIdx < tailIdx) {
                while (!Character.isLetterOrDigit(s.charAt(headIdx))) headIdx++;
                while (!Character.isLetterOrDigit(s.charAt(tailIdx))) tailIdx--;

                if (Character.toUpperCase(s.charAt(headIdx)) != Character.toUpperCase(s.charAt(tailIdx))) {
                    return false;
                }
                headIdx++;
                tailIdx--;
            }
            return true;
        }
        catch (StringIndexOutOfBoundsException ex) {
            return true;
        }    
    }
}
