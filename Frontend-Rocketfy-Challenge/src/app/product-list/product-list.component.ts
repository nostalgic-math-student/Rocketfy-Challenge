import { Component } from '@angular/core';
import product_records from '../data/product_records.json'; 
import { provideProtractorTestingSupport } from '@angular/platform-browser';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {

    product_records = product_records;
}
