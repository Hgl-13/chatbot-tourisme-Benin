export enum Role {
    USER = 'user',
    ASSISTANT = 'assistant'
}

export interface Message {
    role: Role;
    content: string;
}

export interface ChatRequest {
    message: string;
    history?: Message[];
}

export interface ChatResponse {
    response: string;
    source: string[] | null;
}

export interface Conversation {
    id: string;
    title: string;
    date: Date;
    messages: Message[];
}