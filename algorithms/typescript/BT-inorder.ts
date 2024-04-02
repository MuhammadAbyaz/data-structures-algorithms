import { BinaryNode } from "./BT-preorder";

function inorder_walk(curr: BinaryNode<number>, path: number[]): number[] {
  if (!curr) {
    return path;
  }
  inorder_walk(curr.left, path);
  path.push(curr.value);
  inorder_walk(curr.right, path);
  return path;
}
function inorder_search(head: BinaryNode<number>, path: number[]): number[] {
  return inorder_walk(head, []);
}
