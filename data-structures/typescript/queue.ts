type QNode<T> = {
    value:T,
    next?: QNode<T>,
}

class Queue<T>{
    public length: number;
    private head?:QNode<T>;
    private tail?:QNode<T>;
    constructor(){
        this.head = this.tail = undefined;
        this.length = 0;
    }
    enqueue(item: T): void{
        this.length++;
        const node = {value:item}as QNode<T>;
        if(!this.tail){
            this.head = this.tail = node;
            return;
        }
        this.tail.next = node;
        this.tail = this.tail.next;
    }
    dequeue():T | undefined{
        if (!this.head){
            return undefined
        }
        this.length--;
        const head = this.head;
        this.head = this.head.next;
        head.next = undefined;
        return head.value;        
    }
    peek(): T | undefined{
        return this.head?.value;
    }
}