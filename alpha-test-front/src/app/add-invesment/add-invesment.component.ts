import { Component, OnInit } from '@angular/core';
import { AppService } from '../app.service';

export interface IProducto {
  id: number;
  cantidadDiasHoraOperativa: number;
  cantidadDiasHoraNoOperativa: number;
  cantidadDiasHoraOperativaReinversion: number;
  cantidadDiasHoraNoOperativaReinversion: number;
}

export interface IInversion {
  id: number;
  producto: number;
  enReinversion: boolean;
  plazo: number;
  fechaCreacion: string;
}

interface IInversionForm {
  producto: number;
  enReinversion: boolean;
  plazo: number;
}

@Component({
  selector: 'app-add-invesment',
  templateUrl: './add-invesment.component.html',
  styleUrls: ['./add-invesment.component.css'],
  providers: [AppService],
})
export class AddInvesmentComponent implements OnInit {
  constructor(private appService: AppService) {}

  model: IInversionForm = {
    producto: 0,
    enReinversion: false,
    plazo: 1,
  };

  productos: IProducto[] = [];
  inversiones: IInversion[] = [];
  calculoInversion: any;

  ngOnInit() {
    this.getProducts();
  }

  getProducts() {
    this.appService.getProducts().subscribe((data: IProducto[]) => {
      this.productos = data;
    });
  }

  getInversiones() {
    this.appService.getInversiones().subscribe((data: IInversion[]) => {
      this.inversiones = data;
    });
  }

  createInversion() {
    this.appService.createInversion(this.model).subscribe((data) => {
      this.calculoInversion = data;
    });
  }

  onSubmit() {
    if (this.model.plazo === 0 || this.model.producto === 0) {
      alert('Plazo o Producto no puede ser 0');
    } else {
      console.log(this.model);
      this.createInversion();
    }
  }
}
