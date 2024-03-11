function two_crystal_balls(breaks: boolean[]): number {
  const jumpAmnt: number = Math.floor(Math.sqrt(breaks.length));
  let i = jumpAmnt;
  for (; i <= breaks.length; i += jumpAmnt) {
    if (breaks[i]) break;
  }
  i -= jumpAmnt;
  for (let j = 0; j < jumpAmnt && i < breaks.length; j++, i++) {
    if (breaks[i]) return i;
  }
  return -1;
}
