import { Component, ElementRef, ViewChild, AfterViewChecked } from '@angular/core';
import { ChatService } from '@app/services/chat.service';
import { ChatRequest, ChatResponse, Message, Role, Conversation } from '@app/models/model';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';




@Component({
  selector: 'app-chat-box',
  imports: [CommonModule, FormsModule],
  templateUrl: './chat-box.html',
  styleUrl: './chat-box.css',
})
export class ChatBox implements AfterViewChecked {
  @ViewChild('messagesContainer') private messagesContainer!: ElementRef;

  messages: Message[] = [];
  userInput: string = '';
  loading: boolean = false;
  sidebarOpen: boolean = false;
  errorMessage: string = '';

  // historique fictif
  conversations: Conversation[] = [
    { id: '1', title: 'Sites touristiques de Ouidah', date: new Date('2025-03-28'), messages: [] },
    { id: '2', title: 'Histoire du Royaume du Dahomey', date: new Date('2025-03-27'), messages: [] },
    { id: '3', title: 'Gastronomie béninoise', date: new Date('2025-03-25'), messages: [] }
  ];

  private shouldScroll = false;

  constructor(private chatService: ChatService) {}

  ngAfterViewChecked(): void {
    if (this.shouldScroll) {
      this.scrollToBottom();
      this.shouldScroll = false;
    }
  }

  get hasMessages(): boolean {
    return this.messages.length > 0;
  }

  toggleSidebar(): void {
    this.sidebarOpen = !this.sidebarOpen;
  }

  closeSidebar(): void {
    this.sidebarOpen = false;
  }

  selectConversation(conv: Conversation): void {
    // TODO: charger la conversation sélectionnée depuis le backend
    this.closeSidebar();
  }

  newConversation(): void {
    this.messages = [];
    this.errorMessage = '';
    this.closeSidebar();
  }

  sendSuggestion(text: string): void {
    this.userInput = text;
    this.sendMessage();
  }

  sendMessage(): void {
    if (!this.userInput.trim()) return;

    const userMessage: Message = {
      role: Role.USER,
      content: this.userInput
    };
    this.messages.push(userMessage);
    this.shouldScroll = true;
    this.errorMessage = '';

    const request: ChatRequest = {
      message: this.userInput,
      history: this.messages
    };

    this.userInput = '';
    this.loading = true;

    this.chatService.sendMessage(request).subscribe({
      next: (response: ChatResponse) => {
        const assistantMessage: Message = {
          role: Role.ASSISTANT,
          content: response.response
        };
        this.messages.push(assistantMessage);
        this.loading = false;
        this.shouldScroll = true;
      },
      error: (error: any) => {
        console.error('Erreur lors de l\'envoi du message:', error);
        this.loading = false;
        this.errorMessage = 'Le Fâ ne répond pas. Veuillez réessayer.';
        this.shouldScroll = true;
      }
    });
  }

  onKeydown(event: KeyboardEvent): void {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.sendMessage();
    }
  }

  private scrollToBottom(): void {
    try {
      const el = this.messagesContainer?.nativeElement;
      if (el) {
        el.scrollTop = el.scrollHeight;
      }
    } catch (_) {}
  }
}
