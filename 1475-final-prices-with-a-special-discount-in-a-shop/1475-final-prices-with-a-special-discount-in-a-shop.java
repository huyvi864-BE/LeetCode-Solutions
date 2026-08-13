import java.util.Stack;

class Solution {
    public int[] finalPrices(int[] prices) {
        int[] result = prices.clone();
        
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < prices.length; i++) {
            while (!stack.isEmpty() && prices[stack.peek()] >= prices[i]) {
                int index = stack.pop();
                result[index] -= prices[i]; 
            }
            stack.push(i);
        }
        
        return result;
    }
}
