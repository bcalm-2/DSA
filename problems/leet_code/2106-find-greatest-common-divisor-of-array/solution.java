class Solution {
    public int findGCD(int[] nums) {
        int minNum = 1000;
        int maxNum = 0;

        for ( int num : nums ) {
            minNum = Math.min(minNum , num);
            maxNum = Math.max(maxNum , num);
        }

        int ans = 1 ;
        for ( int i = 2 ; i <= maxNum ; i++ ) {
            if( minNum % i == 0 && maxNum % i == 0 ) ans = Math.max(ans , i);
        }

        return ans;
    }
}
