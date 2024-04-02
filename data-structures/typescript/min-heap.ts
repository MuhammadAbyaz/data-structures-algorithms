export default class MinHeap{
    public length: number;
    private data: number[];

    constructor(){
        this.data = [];
        this.length = 0;
    }
    insert(value:number):void{
        this.data[this.length] =value;
        this.heapifyUp(this.length);
        this.length++;
    }
    poll():number{
        if (this.length === 0){
            return -1;
        }
        const out = this.data[0];
        this.length--;
        if (this.length === 0){
            this.data = [];
            return out;
        }
        this.data[0] = this.data[this.length];
        this.heapifyDown(0);
        return out
    }
    private heapifyUp(idx:number):void{
        if (idx === 0){
            return;
        }
        const p = this.parent(idx);
        const parentV = this.data[p];
        const v = this.data[idx];
        if (parentV > v){
            this.data[idx] = parentV;
            this.data[p] = v
            this.heapifyUp(p);
        }
    }
    private heapifyDown(idx:number):void{
        const lIdx = this.leftChild(idx);
        const rIdx = this.rightChild(idx);
        if (idx >= this.length || lIdx >= this.length){
            return;
        }
        const lV = this.data[lIdx]
        const rV = this.data[rIdx]
        const v = this.data[idx]
        if (lV > rV && v > rV){
            this.data[idx] = rV;
            this.data[rIdx] = v;
            this.heapifyDown(rIdx)
        } else if (rV > lV && v > lV){
            this.data[idx] = lV;
            this.data[lIdx] = v;
            this.heapifyDown(lIdx);
        }
    }
    private parent(idx:number):number{
        return Math.floor((idx-1)/2);
    }
    private leftChild(idx:number):number{
        return 2* idx +1
    }

    private rightChild(idx:number):number{
        return 2* idx +2
    }
}