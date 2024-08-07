// mfe1/src/app/remote-entry/entry.module.ts

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { CounterComponent } from '../counter/counter.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    HttpClientModule,
    CounterComponent,
    RouterModule.forChild([
      {
        path: '',
        component: CounterComponent, // Route for the component
        pathMatch: 'full',
      },
    ]),
  ],
  exports: [CounterComponent], // Export the component if needed elsewhere
})
export class RemoteEntryModule {}
