import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'; // Import HttpClient

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.css'],
  standalone: true,
})
export class CounterComponent {
  counterValue: number = 0;
  apiUrl: string = 'http://localhost:8000';

  constructor(private http: HttpClient) {
    this.getCounterValue();
  }

  getCounterValue(): void {
    this.http
      .get<{ value: number }>(`${this.apiUrl}/counter`)
      .subscribe((response) => {
        this.counterValue = response.value;
      });
  }

  increment(): void {
    this.http
      .post<{ value: number }>(`${this.apiUrl}/counter/increment`, {})
      .subscribe((response) => {
        this.counterValue = response.value;
      });
  }

  decrement(): void {
    this.http
      .post<{ value: number }>(`${this.apiUrl}/counter/decrement`, {})
      .subscribe((response) => {
        this.counterValue = response.value;
      });
  }

  reset(): void {
    this.http
      .post<{ value: number }>(`${this.apiUrl}/counter/reset`, {})
      .subscribe((response) => {
        this.counterValue = response.value;
      });
  }
}
