type WeightedAdjacencyMatrix = number[][];
function bfs(
  graph: WeightedAdjacencyMatrix,
  source: number,
  needle: number
): number[] | null {
  const seen = new Array(graph.length).fill(false);
  const previous = new Array(graph.length).fill(-1);
  seen[source] = true;
  const q: number[] = [source];
  do {
    const curr = q.shift() as number;
    if (curr == needle) {
      break;
    }
    seen[curr] = true;
    const adjs = graph[curr];
    for (let i = 0; i < adjs.length; i++) {
      if (adjs[i] === 0) continue;
      if (seen[i]) continue;
      seen[i] = true;
      previous[i] = curr;
      q.push(i);
    }
  } while (q.length);
  if (previous[needle] === -1) return null;
  let curr = needle;
  const out: number[] = [];
  while (previous[curr] != -1) {
    out.push(curr);
    curr = previous[curr];
  }
  return [source].concat(out.reverse());
}
