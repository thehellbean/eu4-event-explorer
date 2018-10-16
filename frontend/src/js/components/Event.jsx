import React, { Component } from 'react';
import { connect } from 'react-redux';
import { eventsFetchData } from '../actions/items';
import classnames from 'classnames';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Collapse from '@material-ui/core/Collapse';
import Avatar from '@material-ui/core/Avatar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import red from '@material-ui/core/colors/red';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import ParameterGrouping from './ParameterGrouping.jsx';

const styles = theme => ({
  card: {
    width: '40%',
    marginLeft: 'auto',
    marginRight: 'auto'
  },
  actions: {
    display: 'flex',
  },
  expand: {
    transform: 'rotate(0deg)',
    transition: theme.transitions.create('transform', {
      duration: theme.transitions.duration.shortest,
    }),
    marginLeft: 'auto',
    [theme.breakpoints.up('sm')]: {
      marginRight: -8,
    },
  },
  expandOpen: {
    transform: 'rotate(180deg)',
  },
});

class Event extends Component {
    constructor(props) {
        super(props);

        this.state = {expanded: false};
    }

    render() {
        const { classes } = this.props;


        let groupings = []
        /*for (var key in this.props.event) {
          if (this.props.event.hasOwnProperty(key) && key !== 'english_desc' && key !== 'english_title' && key === 'trigger' || key === 'mean_time_to_happen') {
            groupings.push(<ParameterGrouping root={this.props.event[key]}/>);
          }
        }*/

        return (
            <Card className={classes.card}>
                <CardContent>
                <Typography variant="headline" component="h2">
                    {this.props.event.english_title}
                </Typography>

                    <Typography component="p">
                        {this.props.event.english_desc}
                    </Typography>
                <CardActions className={classes.actions} disableActionSpacing>
                  <IconButton
                    className={classnames(classes.expand, {
                      [classes.expandOpen]: this.state.expanded,
                    })}
                    onClick={() => { this.setState({ expanded: !this.state.expanded })}}
                    aria-expanded={this.state.expanded}
                    aria-label="Show more"
                    >
                    <ExpandMoreIcon />
                  </IconButton>
                </CardActions>
                </CardContent>
                <Collapse in={this.state.expanded} timeout="auto" unmountOnExit>
                    <CardContent>
                        <ParameterGrouping root={this.props.event}/>
                    </CardContent>
                </Collapse>
            </Card>
            )
    }
};

Event.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Event);
