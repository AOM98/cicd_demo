// /counter-app/src/app/counter/counter.module.ts

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [],
  imports: [CommonModule, HttpClientModule, AppComponent],
  exports: [], // Export the component for use in other modules
})
export class CounterModule {}
