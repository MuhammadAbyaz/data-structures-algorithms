export type BinaryNode<T> = {
  value: number;
  left: BinaryNode<T>;
  right: BinaryNode<T>;
};
function pre_walk(curr: BinaryNode<number> | null, path: number[]): number[] {
  if (!curr) {
    return path;
  }
  path.push(curr.value);

  pre_walk(curr.left, path);
  pre_walk(curr.right, path);

  // post
  return path;
}
function pre_order_search(head: BinaryNode<number>): number[] {
  return pre_walk(head, []);
}
