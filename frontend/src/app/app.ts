import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ChatBox } from '@app/components/chat-box/chat-box';

@Component({
  selector: 'app-root',
  imports: [ChatBox],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('frontend');
}
