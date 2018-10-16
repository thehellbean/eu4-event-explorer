import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import EventList from "./EventList.jsx"
import { eventsFetchData } from '../actions/items.js'
import TopBar from "./TopBar.jsx"
import Search from "./Search.jsx"

export default class App extends Component {
	render() {
	return (
		<>
			<TopBar/>
			<Search/>
			<EventList/>
		</>
		);
	}
}