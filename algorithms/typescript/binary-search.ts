function binary_search(haystack: number[], needle: number): boolean {
  let lo: number = 0;
  let hi: number = haystack.length - 1;
  while (lo < hi) {
    var m: number = Math.floor(hi + lo / 2);
    if (haystack[m] === needle) {
      return true;
    } else if (needle > haystack[m]) {
      lo = m + 1;
    } else {
      hi = m - 1;
    }
  }
  return false;
}
