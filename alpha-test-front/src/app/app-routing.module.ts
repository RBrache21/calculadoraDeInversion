import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddInvesmentComponent } from './add-invesment/add-invesment.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'add-investment', component: AddInvesmentComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
