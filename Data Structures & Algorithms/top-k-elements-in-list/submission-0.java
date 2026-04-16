class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hMap = new HashMap<>();

        for(int num : nums) {
            if(hMap.containsKey(num)) {
                hMap.put(num, hMap.get(num) + 1);
            } else {
                hMap.put(num, 1);
            }
        }

        TreeMap<Integer, ArrayList<Integer>> freqMap = new TreeMap<>(Collections.reverseOrder());
        for(Map.Entry<Integer, Integer> entry : hMap.entrySet()) {
            if(freqMap.containsKey(entry.getValue())) {
                freqMap.get(entry.getValue()).add(entry.getKey());
            } else {
                ArrayList<Integer> freq = new ArrayList<>();
                freq.add(entry.getKey());
                freqMap.put(entry.getValue(), freq);
            }
        }

        ArrayList<Integer> topK = new ArrayList<>();
        for(Map.Entry<Integer, ArrayList<Integer>> entry : freqMap.entrySet()) {
            topK.addAll(entry.getValue());
        }

        return topK.subList(0, k).stream().mapToInt(i -> i).toArray();
    }
}
