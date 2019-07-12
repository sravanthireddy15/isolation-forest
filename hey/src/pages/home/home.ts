import { Component } from '@angular/core';
import { NavController,AlertController} from 'ionic-angular';
import {ViewChild} from '@angular/core';
import {LoginPage} from '../login/login';
import {RegisterPage} from '../register/register';



@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  
  @ViewChild('username')un;
  @ViewChild('password')pw;
  constructor(public navCtrl: NavController,public alertCtrl :AlertController) {
 
  }

  signIn(){
  	this.navCtrl.push(LoginPage);
  }
  Register(){
  	this.navCtrl.push(RegisterPage);
  }


}
