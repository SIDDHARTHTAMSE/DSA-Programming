class Solution {
    public int maxProfit(int[] prices) {
        int i =1;
        int min_profit = prices[0];
        int max_profit = 0;
        while(i <prices.length)
        {
            if(prices[i] < min_profit)
            {
                min_profit = prices[i];
            }
            else
            {
                max_profit = Math.max(max_profit, prices[i] - min_profit);
            }
            i++;
        }
        return max_profit;
    }
}