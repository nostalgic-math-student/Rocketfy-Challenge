import { Component } from '@angular/core';
import product_records from '../data/product_records.json'; 
import { provideProtractorTestingSupport } from '@angular/platform-browser';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {

    // Products from JSON

    product_records = product_records;
  
    // Filter logic

    ngOnInit() {
      
      this.filteredProducts = this.product_records;
    }

    // Filter variables 
    
    filterName: string = '';
    filterCategory: string | null = null;
    filteredProducts: any[] = [];
  
    onCategoryChange(newCategory: string) {
      this.filterCategory = newCategory;
      this.applyFilters();
    }

    applyFilters() {
      this.filteredProducts = this.product_records.filter((product) => {
        const nameMatch = product.name.toLowerCase().includes(this.filterName.toLowerCase());
        const categoryMatch = !this.filterCategory || product.category === this.filterCategory;
        return nameMatch && categoryMatch;
      });
    }
}
