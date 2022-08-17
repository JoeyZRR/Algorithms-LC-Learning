class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left =1;
        int maxV = 0;
        for (int i=0; i < piles.length; i++){
            if (maxV < piles[i]){
                maxV = piles[i];
            }
        }
        int right = maxV;
        while (left < right){
            int mid = left + (right - left)/2;
            int time = curTime(piles, mid);
            if (time > h){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left;

    }
    public int curTime(int [] piles, int k){
        int cur = 0;
        for (int pile: piles){
            if (k >= pile){
                cur += 1;
            }else{
                cur += (k + pile -1) / k;
            }
        }
        return cur;
    }
}