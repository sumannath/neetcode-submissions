class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;

        int islands = 0;

        for(int i = 0 ; i < rows ; i++) {
            for(int j = 0 ; j < cols ; j++) {
                if(grid[i][j] == '1') {
                    dfs(grid, i, j);
                    islands++;
                }
            }
        }

        return islands;
    }

    private void dfs(char[][] grid, int r, int c) {
        int rows = grid.length, cols = grid[0].length;

        if(r >= rows || c >= cols || r < 0 || c < 0 || grid[r][c] == '0') return;

        grid[r][c] = '0';

        dfs(grid, r+1, c);
        dfs(grid, r-1, c);
        dfs(grid, r, c-1);
        dfs(grid, r, c+1);
    }
}
