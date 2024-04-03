type GraphEdge = {
  to: number;
  weight: number;
};
type WeightedAdjacencylist = GraphEdge[][];
function walk(
  graph: WeightedAdjacencylist,
  curr: number,
  needle: number,
  seen: boolean[],
  path: number[]
): boolean {
  if (seen[curr]) {
    return false;
  }
  seen[curr] = true;
  path.push(curr);
  if (curr === needle) {
    return true;
  }
  const list = graph[curr];
  for (let i = 0; i < list.length; ++i) {
    const edge = list[i];
    if (walk(graph, edge.to, needle, seen, path)) {
      return true;
    }
  }
  path.pop();
  return false;
}
function dfs(
  graph: WeightedAdjacencylist,
  source: number,
  needle: number
): number[] | null {
  const seen = Array(graph.length).fill(false);
  const path: number[] = [];
  walk(graph, source, needle, seen, path);
  if (path.length === 0) {
    return null;
  }
  return path;
}
