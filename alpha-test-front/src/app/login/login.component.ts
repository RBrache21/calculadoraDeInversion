import { Component, OnInit } from '@angular/core';
import { AppService } from '../app.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  constructor(private appService: AppService, private router: Router) {}

  model = {
    email: '',
    password: '',
  };

  ngOnInit(): void {}

  onSubmit = () => {
    this.appService.login(this.model).subscribe((data) => {
      console.log(data);
      if (data.access) {
        this.router.navigate(['/add-investment']);
      } else {
        if (data.message) {
          alert(data.message);
        } else {
          alert(data.error);
        }
      }
    });
  };
}
