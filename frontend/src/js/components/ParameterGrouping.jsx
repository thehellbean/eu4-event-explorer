import React, { Component } from 'react';
import Typography from '@material-ui/core/Typography';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { withStyles } from '@material-ui/core/styles';
import Divider from '@material-ui/core/Divider';


const styles = theme => ({
  root: {
    width: '100%',
    backgroundColor: theme.palette.background.paper,
  }
});

class ParameterGrouping extends Component {
	capitalizeFirstLetter(string) {
    	return string.charAt(0).toUpperCase() + string.slice(1);
	}

	readableValue(key, value) {
		if (!isNaN(value) && !key.startsWith("add") && key !== 'days' && key !== 'months') {
			return " ≥ " + value;
		} else {
			return ": " + value;
		}
	}

	readableKey(key) {
		switch (key) {
			case 'NOT':
				return "The following must not be true:";

			case 'OR':
				return "One of the following must be true:";

			case "AND":
				return "All of the following must be true:";
			default:
				return this.capitalizeFirstLetter(key.replace(/_/g, " "));
		}
	}

	recurseParameters(obj, depth=0) {
		const { classes } = this.props;
		
		if (typeof obj !== 'object') {
			return [(<ListItem className={classes.nested} style={{paddingLeft: depth*20}}>
					 <ListItemText inset primary={obj}/>
					 </ListItem>)];
		}
		let jsxlist = [];
		let start = 0;
		if (obj.hasOwnProperty(start)) {
			while (obj.hasOwnProperty(start)) {
				jsxlist.push(this.recurseParameters(obj[start], depth + 1));
				jsxlist.push(<Divider/>);
				start++;
			}
		} else {
			for (var key in obj) {
				if (obj.hasOwnProperty(key)) {
					if (typeof obj[key] === 'object') {
						jsxlist.push(<ListItem className={classes.nested} style={{paddingLeft: depth * 20}} button>
									<ListItemText inset primary={this.readableKey(key)} />
									</ListItem>,
									<List component="div" disablePadding style={{backgroundColor: 'rgba(0, 0, 0, 0.1)'}}>
										{this.recurseParameters(obj[key], depth + 1)}
									</List>,
									<Divider style={{borderColor: 'red', width: 200, marginLeft: depth * 30 + 50}}/>);
					} else {
						jsxlist.push(
							<ListItem style={{paddingLeft: depth * 20}} className={classes.nested} button>
							<ListItemText inset primary={this.readableKey(key) + this.readableValue(key, obj[key])}/>
							</ListItem>);
					}
				}
			}
		}
		return jsxlist;
	}

	render() {
		const { classes } = this.props;
		let listElements = [];
		for (var key in this.props.root) {
					if (this.props.root.hasOwnProperty(key)) {
						listElements.push(<ListItem>{key}</ListItem>)
					}
				}
		return (<List component="div" className={classes.root} style={{marginLeft: 0}}>
			{
				this.recurseParameters(this.props.root)
			}
		</List>)
	}
};

export default withStyles(styles)(ParameterGrouping);