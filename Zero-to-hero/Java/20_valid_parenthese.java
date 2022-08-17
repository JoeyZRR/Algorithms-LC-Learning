// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
//  

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false



class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for (char ch: s.toCharArray()){
            if (ch == '(') st.push(')');
            else if(ch == '[') st.push(']');
            else if(ch == '{') st.push('}');
            else if(st.isEmpty()||ch!=st.pop()) return false;
        }
        return st.isEmpty();
    }
}