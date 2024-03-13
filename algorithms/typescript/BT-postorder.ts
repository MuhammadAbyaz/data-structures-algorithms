function post_walk(curr: BinaryNode<number> | null, path: number[]): number[] {
  if (!curr) {
    return path;
  }
  post_walk(curr.left, path);
  post_walk(curr.right, path);
  path.push(curr.value);
  return path;
}
function post_order_search(head: BinaryNode<number>, path: number[]): number[] {
  return post_walk(head, []);
}
