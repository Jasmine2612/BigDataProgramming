

import java.io.*; 

public class CommonSubSequence 
{ 
	 String lcs(String Str1, String Str2, int x, int y) 
	{ 
		 int[][] arr = new int[x + 1][y + 1];
		 
	        for (int i = x - 1; i >= 0; i--)
	        {
	            for (int j = y - 1; j >= 0; j--)
	            {
	                if (Str1.charAt(i) == Str2.charAt(j))
	                    arr[i][j] = arr[i + 1][j + 1] + 1;
	                else 
	                    arr[i][j] = Math.max(arr[i + 1][j], arr[i][j + 1]);
	            }
	        }
	 
	        int i = 0, j = 0;
	        StringBuffer sb = new StringBuffer();
	        while (i < x && j < y) 
	        {
	            if (Str1.charAt(i) == Str2.charAt(j)) 
	            {
	                sb.append(Str1.charAt(i));
	                i++;
	                j++;
	            }
	            else if (arr[i + 1][j] >= arr[i][j + 1]) 
	                i++;
	            else
	                j++;
	        }
	        return sb.toString();
	    }

	 
	

	public static void main (String[] args) throws IOException 
	{ 
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Longest Common Subsequence");
 
        System.out.println("Enter string 1");
        String Str1 = br.readLine();
 
        System.out.println("Enter string 2");
        String Str2 = br.readLine();
 
        
		int x = Str1.length(); 
		int y = Str2.length(); 
		Str1 = Str1.toLowerCase();
		Str2 = Str2.toLowerCase();
		
		CommonSubSequence rs = new CommonSubSequence();
		
		String result = rs.lcs(Str1, Str2, x, y); 
		
		System.out.println("Common subsequence of  "+Str1+" and "+Str2+" is: "+ result); 
		
	} 
} 


