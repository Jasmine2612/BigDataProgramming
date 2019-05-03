import java.io.*;


public class PatternMatching {
	
	public static boolean isMatching(String str, String pattern)
	{
	
		int n = str.length();
		int m = pattern.length();
		

		boolean[][] T = new boolean[n+1][m+1];

		
		T[0][0] = true; // if both pattern and String is empty

		// empty String case
		for (int j = 1; j <= m; j++) {
			if (pattern.charAt(j - 1) == '*') {
				T[0][j] = T[0][j - 1];
			}
		}

		// Matrix approach
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (pattern.charAt(j-1) == '*') {
					T[i][j] = T[i - 1][j] || T[i][j - 1];
				}
				else if (pattern.charAt(j-1) == '.' ||
						str.charAt(i-1) == pattern.charAt(j-1)) {
					T[i][j] = T[i - 1][j - 1];
				}
			}
		}

	
		return T[n][m];
	} 

	public static void main(String[] args) throws IOException
	{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Pattern Matching");
 
        System.out.println("Enter string 1");
        String str = br.readLine();
 
        System.out.println("Enter string 2");
        String pattern = br.readLine();
 
	

		if (isMatching(str, pattern)) {
			System.out.println("Pattern Matching  "+str+" and "+pattern+" is: True");
		}
		else {
			System.out.println("Pattern Matching  "+str+" and "+pattern+" is: False ");
		}
	}
}
