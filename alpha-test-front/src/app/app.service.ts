import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AppService {
  constructor(private http: HttpClient) {}

  baseurl = 'http://127.0.0.1:8000';
  httpheaders = new HttpHeaders({
    'Content-Type': 'application/json',
  });

  login(user: any): Observable<any> {
    return this.http.post(`${this.baseurl}/login/`, user, {
      headers: this.httpheaders,
    });
  }

  getProducts(): Observable<any> {
    return this.http.get(`${this.baseurl}/productos/`, {
      headers: this.httpheaders,
    });
  }

  getInversiones(): Observable<any> {
    return this.http.get(`${this.baseurl}/inversiones/`, {
      headers: this.httpheaders,
    });
  }

  createInversion(inversion: any): Observable<any> {
    return this.http.post(`${this.baseurl}/crear-inversion/`, inversion, {
      headers: this.httpheaders,
    });
  }
}
