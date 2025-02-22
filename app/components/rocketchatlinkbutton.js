import React from 'react';
import { NavLink } from 'react-bootstrap';

const RocketChatLinkButton = ({
  children,
  href = 'https://open.rocket.chat/channel/DemoDay2022',
  ...props
}) => {
  return (
    <NavLink target="_blank" href={href} {...props}>
      {children}
    </NavLink>
  );
};

export default RocketChatLinkButton;
