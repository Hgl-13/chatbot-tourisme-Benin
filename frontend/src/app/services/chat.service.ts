import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';  
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Message, ChatRequest, ChatResponse } from '@app/models/model';

@Injectable({
  providedIn: 'root'
})
export class ChatService{
    private apiUrl = environment.apiUrl;
    constructor(private http: HttpClient) {}

    sendMessage(request: ChatRequest): Observable<ChatResponse> {
        return this.http.post<ChatResponse>(`${this.apiUrl}/chat`, request);
    }
}