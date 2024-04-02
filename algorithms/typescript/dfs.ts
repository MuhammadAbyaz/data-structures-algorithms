import { BinaryNode } from "./BT-preorder";
function search(curr: BinaryNode<number> | null, needle: number) {
  if (!curr) {
    return false;
  }
  if (curr.value === needle) {
    return true;
  }
  if (curr.value < needle) {
    return search(curr.right, needle);
  }
  return search(curr.left, needle);
}
function dfs(head: BinaryNode<number>, needle: number) {
  return search(head, needle);
}
